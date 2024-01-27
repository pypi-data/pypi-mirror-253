# dapla-statbank-client
Used internally by SSB (Statistics Norway).
Validates and transfers data from Dapla to Statbank.
Gets data from public and internal statbank.


### Installing from Pypi with Poetry
If your project has been set up with `ssb-project create`, navigate into the folder with the terminal. `cd project-name`. Then install the package:
```bash
poetry add dapla-statbank-client
ssb-project build
```
Make a notebook with the project's kernel, try this code to verify that you can "log in":
```python
from statbank import StatbankClient
stat_client = StatbankClient(loaduser = "LASTEBRUKER")
# Change LASTEBRUKER to your load-statbank-username
# Fill out password
# Default publishing-date is TOMORROW
print(stat_client)
# Printing will show you all the default settings on the client.
# You can change for example date by specifying it: StatbankClient(loaduser = "LASTEBRUKER", date="2023-02-16")
```

Be aware that from the **dapla-staging environment** you will be sending to statbank-TEST-database, your changes will not be published. For this you need the "test-password", which is for the same user (lastebruker), but different from the ordinary password (lastepassord). If you are missing the test-password, have the statbank-team send it to you for you loaduser. If you are in the main dapla-jupyterlab (prod), you **WILL** publish to statbanken, in the PROD database. So pay extra attention to the **publishing-date** when in dapla-main-prod-jupyterlab. And be aware of which password you are entering, based on your environment. [To see data actually published to the test-database, you can use this link if you work at SSB.](https://i.test.ssb.no/pxwebi/pxweb/no/test_24v_intern/)


### Usage Transferring

```python
stat_client.transfer({"deltabellfilnavn.dat" : df_06399}, "06339")
```
The simplest form of usage, is directly-transferring using the transfer-method under the client-class. The statbanktable expects named "deltabeller" in a dictionary, see `trasferdata_template()` below. This might be all you need if this data has been sent in the same shape to statbanken before... If you are unsure at all, keep reading.


### Building datasets
You can look at the "filbeskrivelse" which is returned from `stat_client.get_description()` in its own local class: StatbankUttrekksBeskrivelse
```python
description_06339 = stat_client.get_description(tableid="06339")
print(description_06339)
```
This should have all the information you are used to reading out from the old "Filbeskrivelse". And describes how you should construct your data.

Your data must be placed in a datastructure, a dict of pandas dataframes. Take a look at how the dict should be constructed with:
```python
description_06339.transferdata_template()
```
This both returns the dict, and prints it, depending on what you want to do with it. Use it to insert your own DataFrames into, and send it to .validate() and/or .transfer(). It might look like this:
```python
{"deltabellfilnavn.dat" : df_06399}
```

Other interesting attributes can be retrieved from the UttrekksBeskrivelse-object:
```python
description_06339.subtables
description_06339.variables
description_06339.codelists
description_06339.suppression
```

After starting to construct your data, you can validate it against the Uttrekksbeskrivelse, using the validate-method, *without starting a transfer*, like this:
```python
stat_client.validate({"deltabellfilnavn.dat" : df_06399}, tableid="06339")
```
Validation will happen by default on user-side, in Python.
Validation happens on the number of tables, number of columns, code usage in categorical columns, code usage in "suppression-columns" (prikkekolonner), and on timeformats (both length and characters used) and more.
**This might be a lot of feedback**, but understanding this will help you to debug what might be wrong with your data, before sending it in.
If your data contains floats, it might hint at you to use the .round_data()-method to prepare your data, it uses the amount of decimals defined in UttrekksBeskrivelse to round UPWARDS (from pure 0.5 values) and convert to strings with comma as the decimal sign along the way, it is used like this:
```python
data_dict_06339 = description_06339.round_data({"deltabellfilnavn.dat" : df_06399})
```




### Getting apidata

These functions can be imported directly and will then not ask for username and password, but are also available through the client...
```python
from statbank import apidata_all, apidata, apidata_rotate
```

```python
df_06339 = apidata_all("06339", include_id=True)
```
`apidata_all`, does not need a specified query, it will build its own query, trying to get *all the data* from the table. This might be too much, resulting in an error.

The `include_id`-parameter is a bit *magical*, it gets both codes and value-columns for categorical columns, and tries to merge these next to each other, it also makes a check if the content is the same, then it will not include the content twice.

If you want to specify a query, to limit the response, use the method `apidata` instead.\
Here we are requesting an "internal table" which only people at SSB have access to, with a specified URL and query.
```python
query = {'query': [{'code': 'Region', 'selection': {'filter': 'vs:Landet', 'values': ['0']}}, {'code': 'Alder', 'selection': {'filter': 'vs:AldGrupp19', 'values': ['000', '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119+']}}, {'code': 'Statsbrgskap', 'selection': {'filter': 'vs:Statsborgerskap', 'values': ['000']}}, {'code': 'Tid', 'selection': {'filter': 'item', 'values': ['2022']}}], 'response': {'format': 'json-stat2'}}

df_folkemengde = apidata("https://i.ssb.no/pxwebi/api/v0/no/prod_24v_intern/START/be/be01/folkemengde/Rd0002Aa",
                                     query,
                                     include_id = True
                                    )
```

`apidata_rotate` is a thin wrapper around pivot_table. Stolen from: https://github.com/sehyoun/SSB_API_helper/blob/master/src/ssb_api_helper.py
```python
df_folkemengde_rotert = apidata_rotate(df_folkemengde, 'tidskolonne', "verdikolonne")
```


### Using a date-widget for publish day
For easier setting of the date on the client, after it has been initialized, you can use a date-picker in JupyterLab from ipywidgets.
```python
date = stat_client.date_picker()
date
# Do a cell shift here, run the cell above and then change the date, dont run the cell again
# When this is then run, it should update the date on the client:
stat_client.set_publish_date(date)
```


### Saving and restoring Uttrekksbeskrivelser and Transfers as json

From `stat_client.transfer()` you will recieve a StatbankTransfer object, from `stat_client.get_description` a StatbankUttrekksBeskrivelse-object. These can be serialized and saved to disk, and later be restored, maybe this can be a form of logging on which transfers were done?

```python
filbesk_06339 = stat_client.get_description("06339")
filbesk_06339.to_json("path.json")
# Later the file can be restored with
filbesk_06339_new = stat_client.read_description_json("path.json")
```
Some deeper data-structures, like the dataframes in the transfer will not be serialized and stored with the transfer-object in its json.

---

### Version history
- 1.0.6 fixing new functionality on "IRkodelister"
- 1.0.5 Making transferdata_template smarter, were it can take a bunch of dataframes and incorporate them in the returned dict. Trying to support columntype "internasjonal rapportering".
- 1.0.4 Fixing bug where empty codelists stops description initialization, Updating pyjstat to 2.4.0, changing imports to absolute from package root
- 1.0.2 Doc-string style cleanup, a check on username and password on client init, changes to time and display of time, demo notebooks cleaned
- 1.0.0 Finished going through initial issues, less complaining from verify on floats
- 0.0.11 Statbank people wanted a user-agent-requesst-header to differentiate test from prod
- 0.0.9 After further user-testing and requests
- 0.0.5 Still some parameter issues
- 0.0.4 More test coverage, some bugs fixed in rounding checks and parameter-passing
- 0.0.3 Removed batches, stripping uttrekk from transfer, rounding function on uttrekk, data required in as a dict of dataframes, with "deltabell-navn". Tableid now works to transfer to instead of only "hovedtabellnavn"
- 0.0.2 Starting alpha, fine-tuning release to Pypi on github-release
- 0.0.1 Client, transfer, description, apidata. Quite a lot of work done already. Pre-alpha.
