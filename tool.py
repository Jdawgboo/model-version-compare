"""Compare model metadata and feature signatures."""
from __future__ import annotations

def compare(before:dict,after:dict)->dict:
 b_features=before.get('features',{});a_features=after.get('features',{});shared=set(b_features)&set(a_features)
 return {'added_features':sorted(set(a_features)-set(b_features)),'removed_features':sorted(set(b_features)-set(a_features)),'changed_features':sorted(key for key in shared if b_features[key]!=a_features[key]),'version_changed':before.get('version')!=after.get('version')}
def breaking(result:dict)->bool:return bool(result['removed_features'] or result['changed_features'])
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);result=compare(p['before'],p['after']);result['breaking']=breaking(result);print(json.dumps(result,indent=2))
