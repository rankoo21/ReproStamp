import json, pytest
from harness import load, UserError

@pytest.fixture
def env(): return load('repro_stamp.py','ReproStamp')

def test_submit_and_audit(env):
    _, c, _, q, w, _ = env
    c.submit_study('STUDY-1','A reproducible test','The method can be rerun from the published artifacts.','https://paper.example/a','https://code.example/a','https://data.example/a')
    bodies=['paper has method and results with enough detail for validation and repeatability','code contains runnable instructions and a tested entry point for readers','data has a documented schema and enough context to reproduce the experiment']
    w.extend(bodies + bodies)
    q.extend(['{"verdict":"REPRODUCIBLE","findings":["The method and artifacts align."]}'] * 2)
    c.audit_study('study-1')
    r=json.loads(c.get_study('0xowner','STUDY-1'))
    assert r['status']=='AUDITED' and r['verdict']=='REPRODUCIBLE' and len(r['digests'])==3

def test_hosts_and_duplicate(env):
    _, c, _, _, _, _ = env
    with pytest.raises(UserError): c.submit_study('BAD','Valid title','This is a sufficiently long claim for a study.','http://paper.example/a','https://code.example/a','https://data.example/a')
    c.submit_study('STUDY-1','A title','This is a sufficiently long claim for a study.','https://paper.example/a','https://code.example/a','https://data.example/a')
    with pytest.raises(UserError): c.submit_study(' study-1 ','Other title','This is a sufficiently long claim for another study.','https://x.example/a','https://y.example/a','https://z.example/a')

def test_malformed_consensus_fails(env):
    _, c, _, q, w, _ = env
    c.submit_study('STUDY-2','A reproducible test','This is a sufficiently long claim for a study.','https://paper.example/a','https://code.example/a','https://data.example/a')
    w.extend(['paper text that is long enough for the audit','code text that is long enough for the audit','data text that is long enough for the audit'])
    q.append('{}')
    with pytest.raises((ValueError,UserError)): c.audit_study('STUDY-2')
