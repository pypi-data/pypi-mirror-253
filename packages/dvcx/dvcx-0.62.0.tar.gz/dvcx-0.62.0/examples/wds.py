from dql.lib.dataset import Dataset
from dql.lib.webdataset import WebDataset
from dql.lib.webdataset_meta import parse_wds_meta
from dql.query.schema import C, DatasetRow

wds = (
    Dataset("s3://dvcx-datacomp-small/shards")
    .filter(C.name.glob("00000000.tar"))
    .generate(WebDataset())
)

meta = (
    Dataset("s3://dvcx-datacomp-small/metadata")
    .filter(C.name.glob("0020f*"))
    .apply(parse_wds_meta)
    .select_except(*DatasetRow.schema.keys())
)

res = wds.join(meta, "uid")

df = res.limit(50).to_pandas()
print(df.columns)
print(df)
