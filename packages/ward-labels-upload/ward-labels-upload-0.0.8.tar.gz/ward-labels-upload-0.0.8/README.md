# Ward Analytics Labels Upload Utility

This utility is used to upload labels to the Ward Analytics Database.

It is for internal use only.

## Installation

```bash
pip install ward-labels-upload
```

## Usage

### The Label Object

The `Label` object is used to represent a label. It has three fields:
- `address`: The address of the label.
- `label`: The label itself.
- `description`: A description of the label.

It also has a `is_address_case_sensitive` field, which defaults to `False`. This field is used to determine whether the address field should be treated as case sensitive or not. In most cases, this field should be left as `False` (For blockchains such as Ethereum, addresses are not case sensitive).

``` python
from ward_labels_upload import Label

label = Label(address="0x12eF3", label="label1", description="description1")
print(label)

>>> Label(address="0x12ef3", label="label1", description="description1", is_address_case_sensitive=False)
```

``` python
from ward_labels_upload import Label

label = Label(address="0x12eF3", label="label1", description="description1", is_address_case_sensitive=True)
print(label)

>>> Label(address="0x12eF3", label="label1", description="description1", is_address_case_sensitive=True)
```

### Label Upload

```python
from ward_labels_upload import Label, LabelUploader

uploader = LabelUploader(api_key="your_api_key")

labels = [
    Label(address="0x12ef3", label="label1", description="description1"),
    Label(address="0x45af6", label="label2", description="description2"),
    Label(address="0x78cs9", label="label3", description="description3"),
]

uploader.upload_labels(labels=labels)
```
The `LabelUploader` class also takes an optional `base_url` parameter. This is the base URL of the Ward Analytics API. It defaults to `https://api.wardanalytics.net`, which is the production API.

### Label Deletion

```python
from ward_labels_upload import Label, LabelUploader

uploader = LabelUploader(api_key="your_api_key")

labels = [
    Label(address="0x12ef3", label="label1"),
    Label(address="0x45af6", label="label2"),
    Label(address="0x78cs9", label="label3"),
]

uploader.delete_labels(labels=labels)
```
In the case of deletion, the description field is unnecessary. This happens because a label is uniquely identified by the combination of its address and label.

### Label Retrieval

```python
from ward_labels_upload import Label, LabelUploader

uploader = LabelUploader(api_key="your_api_key")

addresses = [
    "0x12ef3",
    "0x45af6",
    "0x78cs9",
]

labels = uploader.get_labels(addresses=addresses)
```