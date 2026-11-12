#!/opt/homebrew/opt/python@3.14/bin/python3.14
# Graphify over the OpenLive fork (WINGSCRUM-557). Single pass (943 tracked files). Output: <repo>/foxmap/graphify-out/.
# Same stock graphify 0.4.8 + our .mjs/.cjs/.mts/.cts adapter as the OpenClaw run (raven/tools/_v19/graphify_fork.py).
import os, sys, json, time, collections, subprocess
from pathlib import Path
REPO = Path(sys.argv[1] if len(sys.argv) > 1 else '/Users/clawdbot/research/openlive')
OUT = REPO / 'foxmap' / 'graphify-out'; OUT.mkdir(parents=True, exist_ok=True)
def log(m): print(time.strftime('%H:%M:%S'), m, flush=True)
import graphify.extract as GE
from graphify.extract import _extract_generic, _TS_CONFIG, _JS_CONFIG
STOCK = {'.py': GE.extract_python, '.js': GE.extract_js, '.jsx': GE.extract_js, '.ts': GE.extract_js, '.tsx': GE.extract_js, '.rs': GE.extract_rust,
         '.swift': GE.extract_swift, '.m': GE.extract_objc, '.mm': GE.extract_objc, '.c': GE.extract_c, '.h': GE.extract_c, '.cpp': GE.extract_cpp, '.kt': GE.extract_kotlin}
ADAPT = {'.mjs': lambda p: _extract_generic(p, _JS_CONFIG), '.cjs': lambda p: _extract_generic(p, _JS_CONFIG), '.mts': lambda p: _extract_generic(p, _TS_CONFIG), '.cts': lambda p: _extract_generic(p, _TS_CONFIG)}
DISPATCH = dict(STOCK); DISPATCH.update(ADAPT)
tracked = subprocess.run(['git', '-C', str(REPO), 'ls-files'], capture_output=True, text=True).stdout.split('\n')
tracked = [t for t in tracked if t and not t.startswith('foxmap/')]
code = [REPO / t for t in tracked if Path(t).suffix in DISPATCH]
nodes, edges, errors = [], [], []; per_ext = collections.Counter()
t0 = time.time()
for p in code:
    try:
        r = DISPATCH[p.suffix](p)
        if isinstance(r, tuple): n, e = r[0], r[1]
        else: n, e = r.get('nodes', []), r.get('edges', [])
        for x in n: x.setdefault('source_file', str(p))
        nodes += n; edges += e; per_ext[p.suffix] += 1
    except Exception as ex: errors.append([str(p), repr(ex)[:200]])
log(f'extracted {len(code)} files in {time.time()-t0:.0f}s: nodes={len(nodes)} edges={len(edges)} errors={len(errors)} per_ext={dict(per_ext)}')
try: GE._resolve_cross_file_imports(nodes, edges)
except Exception as ex: log('cross-file resolve skipped: ' + repr(ex)[:120])
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.export import to_json
from graphify.report import generate
ext = dict(nodes=nodes, edges=edges, input_tokens=0, output_tokens=0)
G = build_from_json(ext); comms = cluster(G); coh = score_all(G, comms)
gods = god_nodes(G, top_n=40); surp = surprising_connections(G, comms, top_n=40)
labels = {}
for cid, mem in comms.items():
    c = collections.Counter('/'.join(G.nodes[m].get('source_file', '').replace(str(REPO) + '/', '').split('/')[:3]) for m in mem)
    labels[cid] = (c.most_common(1)[0][0] or 'misc') + f' #{cid}'
qs = suggest_questions(G, comms, labels)
detection = dict(total_files=len(code), total_words=0, files={'code': [str(p) for p in code]})
report = generate(G, comms, coh, labels, gods, surp, detection, {'input': 0, 'output': 0}, str(REPO), suggested_questions=qs)
(OUT / 'GRAPH_REPORT.md').write_text(report)
to_json(G, comms, str(OUT / 'graph.json'))
json.dump(dict(gods=gods, surprises=surp, cohesion={str(k): v for k, v in coh.items()}, questions=qs, labels=labels), open(OUT / 'analysis.json', 'w'), indent=1, default=str)
# file → community/feature index (raw): every tracked file with its node count, its community label, its top symbols
by_file = collections.defaultdict(list)
for nid, d in G.nodes(data=True): by_file[d.get('source_file', '')].append(dict(id=nid, label=d.get('label', nid), type=d.get('type', '')))
comm_of = {m: cid for cid, mem in comms.items() for m in mem}
index = []
for t in tracked:
    p = str(REPO / t); ns = by_file.get(p, [])
    cids = collections.Counter(comm_of.get(n['id']) for n in ns if comm_of.get(n['id']) is not None)
    index.append(dict(file=t, nodes=len(ns), community=labels.get(cids.most_common(1)[0][0]) if cids else None, symbols=[n['label'] for n in ns[:12]]))
json.dump(index, open(OUT / 'file_index.json', 'w'), indent=1)
json.dump(dict(repo=str(REPO), head=subprocess.run(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(), tracked=len(tracked), code_files=len(code),
               nodes=G.number_of_nodes(), edges=G.number_of_edges(), communities=len(comms), errors=errors, per_ext=dict(per_ext), seconds=round(time.time() - t0)), open(OUT / 'summary.json', 'w'), indent=1)
log(f'done: nodes={G.number_of_nodes()} edges={G.number_of_edges()} communities={len(comms)} graph.json={(OUT/"graph.json").stat().st_size} bytes')
