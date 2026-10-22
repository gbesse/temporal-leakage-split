import unittest
from temporal_leakage_split import run

def row(id,t,group=None,label=None):return dict(id=id,time=t,available_at=t,label_available_at=t if label is None else label,group=group)
class DomainTests(unittest.TestCase):
 def test_shared_lineage_purged_only_from_training(self):
  r=run({'cut':10,'evaluation_at':20,'rows':[row('a',1,'g'),row('b',11,'g'),row('c',2,'h')]});self.assertEqual(r['train'],['c']);self.assertEqual(r['test'],['b']);self.assertEqual(r['purged'][0]['reasons'],['lineage_crosses_split'])
 def test_future_label_not_available_at_cut(self):
  r=run({'cut':10,'rows':[row('a',1,label=11)]});self.assertEqual(r['train'],[])
 def test_embargo_and_cut_boundary(self):
  r=run({'cut':10,'embargo':2,'evaluation_at':10,'rows':[row('a',7),row('b',8),row('c',10)]});self.assertEqual(r['train'],['a']);self.assertEqual(r['test'],['c'])
 def test_transitive_links(self):
  r=run({'cut':10,'evaluation_at':20,'rows':[row('a',1),row('b',2),row('c',11)],'links':[['a','b'],['b','c']]});self.assertEqual(r['train'],[])
 def test_unavailable_test_labels_purged(self):self.assertEqual(run({'cut':10,'evaluation_at':12,'rows':[row('a',11,label=15)]})['test'],[])
