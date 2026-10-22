from .common import integer,identifier,unique_ids

def run(data):
    rows=data['rows'];cut=integer(data['cut'],0,10**12);embargo=integer(data.get('embargo',0),0,10**12);evaluation=integer(data.get('evaluation_at',cut),cut,10**12)
    if len(rows)>10000:raise ValueError('size')
    ids=unique_ids(rows);parent={k:k for k in ids}
    def find(k):
        while parent[k]!=k:parent[k]=parent[parent[k]];k=parent[k]
        return k
    def union(a,b):
        if a not in parent or b not in parent:raise ValueError('link')
        parent[find(a)]=find(b)
    groups={}
    for r in rows:
        integer(r['time'],0,10**12);integer(r['available_at'],r['time'],10**12);integer(r['label_available_at'],r['time'],10**12)
        if r.get('group') is not None:
            group=identifier(r['group'])
            if group in groups:union(r['id'],groups[group])
            else:groups[group]=r['id']
    if len(data.get('links',[]))>10000:raise ValueError('links')
    for a,b in data.get('links',[]):union(a,b)
    test_components={find(r['id']) for r in rows if r['time']>=cut};train=[];test=[];purged=[]
    for r in rows:
        reasons=[]
        if r['time']<cut:
            if find(r['id']) in test_components:reasons.append('lineage_crosses_split')
            if r['time']>=cut-embargo:reasons.append('embargo')
            if max(r['available_at'],r['label_available_at'])>cut:reasons.append('not_available_at_training_cut')
            destination=train
        else:
            if max(r['available_at'],r['label_available_at'])>evaluation:reasons.append('not_available_at_evaluation')
            destination=test
        if reasons:purged.append({'id':r['id'],'reasons':reasons})
        else:destination.append(r['id'])
    return {'train':train,'test':test,'purged':purged,'component':{k:find(k) for k in ids},'cut':cut,'evaluation_at':evaluation,'scope':'declared entity/lineage graph and timestamps; cannot detect undisclosed duplicates'}
