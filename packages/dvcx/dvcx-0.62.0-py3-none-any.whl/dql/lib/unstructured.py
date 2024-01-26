import shutil
import tempfile

from unstructured.partition.auto import partition
from unstructured.staging.base import convert_to_dataframe

from dql.query import Object, udf
from dql.sql.types import JSON, String


def encode_object(raw):
    fname = str(raw).replace(">", "").replace("<", "")
    output = tempfile.TemporaryFile()
    shutil.copyfileobj(raw, output)
    elements = partition(file=output, metadata_filename=fname)
    output.close()
    return elements


@udf(
    params=(Object(encode_object),),  # Columns consumed by the UDF.
    output={
        "elements": JSON,
        "title": String,
        "text": String,
        "error": String,
    },  # Signals being returned by the UDF.
)
def partition_object(elements):
    title = str(elements[0])
    text = "\n\n".join([str(el) for el in elements])
    df = convert_to_dataframe(elements)
    return (df.to_json(), title, text, "")
