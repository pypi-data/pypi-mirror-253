# EurostatNode Implementation
This drb-impl-eurostat module implements access to Eurostat data with DRB data model.

## Eurostat Factory
The module implements the basic factory model defined in DRB in its node resolver. Based on the python entry point mechanism, this module can be dynamically imported into applications.

The entry point group reference is `drb.driver`.<br/>
The implementation name is `eurostat`.<br/>
The factory class is encoded into `drb.drivers.eurostat.drb_impl_eurostat`.<br/>

The Eurostat factory creates a `DrbEurostatServiceNode` if called with the path 'eurostat://' or `DrbEurostatDateNode` if a dataset or tables code is given in the path 'eurostat://{code}'.

## Nodes
### DrbEurostatServiceNode
Represent a node for browsing Eurostat data.
Its attribute *tables* contain the list of all the available dataset and tables in the eurostat service.
Its children is a list of `DrbEurostatDataNode` that can be browsed by dataset or table code.
This node has no implementations.

### DrbEurostatDataNode
Represent an Eurostat dataset or table.
Its attribute "columns" contain the list of the data available in this dataset or table. Its children is a list of `DrbEurostatRowNode` that can be browsed only by its index in the table.
A panda DataFrame representation is available using the `get_impl(panda.core.frame.DataFrame)` method

### DrbEurostatRowNode
Represent a single row of an eurostat dataset or table.
Its attribute "columns" contain the list of the data available in this row.
Its children is a list of `DrbEurostatValueNode` that can be browsed by index or name of the column.
This node has noimplementations.

### DrbEurostatValueNode
Represent a single Eurostat cell value from a dataset or table.

## limitations
The current version does not manage child modification and insertion.

## Using this module
To include this module into your project, the `drb-impl-eurostat` module shall be referenced into `requirement.txt` file, or the following pip line can be run:

```commandline
pip install drb-driver-eurostat
```

## Examples
This example create a `DrbEurostatServiceNode` using the `DrbEurostatFactory` then look for tables containing the word 'crimes' using the attribute of the service:

```python
from drb.drivers.eurostat import DrbEurostatFactory

factory = DrbEurostatFactory()
service = factory.create('eurostat://')

tables = service @ 'tables'
search = 'crimes'
for table in tables:
    if search in table[0].lower():
        print(table)
```

Output :

```
('Crimes recorded by the police by NUTS 3 regions', 'crim_gen_reg')
('Crimes recorded by the police by metropolitan regions', 'met_crim_gen')
('Crimes recorded by the police by other typologies', 'urt_crim_gen')
('Crimes recorded by the police by by offence category', 'crim_gen')
('Crimes recorded by the police by NUTS 3 regions', 'crim_gen_reg')
('Crimes recorded by the police: homicide in cities', 'crim_hom_city')
('Crimes recorded by the police (1950-2000)', 'crim_hist')
```

We can get the table we want using its code and get a pandas' DataFrame representation

```python
from pandas.core.frame import DataFrame
from drb.drivers.eurostat import DrbEurostatFactory

code = 'crim_gen_reg'
factory = DrbEurostatFactory()
service = factory.create('eurostat://')
table = service[code]
print(table.get_impl(DataFrame))
```

We can also put the code direcly in the path given to the factory
```python
from pandas.core.frame import DataFrame
from drb.drivers.eurostat import DrbEurostatFactory

code = 'crim_gen_reg'
factory = DrbEurostatFactory()
table = factory.create('eurostat://' + code)
print(table.get_impl(DataFrame))
```

Output: 

```
     unit        iccs geo\time   2010    2009   2008
0      NR    ICCS0101       AT   56.0    43.0   46.0
1      NR    ICCS0101      AT1   33.0    23.0   21.0
2      NR    ICCS0101     AT11    5.0     0.0    2.0
3      NR    ICCS0101     AT12   11.0     4.0    4.0
4      NR    ICCS0101     AT13   17.0    19.0   15.0
...   ...         ...      ...    ...     ...    ...
5581   NR  ICCS050211    UKN01  843.0  1025.0  987.0
5582   NR  ICCS050211    UKN02  434.0   443.0  476.0
5583   NR  ICCS050211    UKN03  454.0   525.0  549.0
5584   NR  ICCS050211    UKN04  358.0   340.0  336.0
5585   NR  ICCS050211    UKN05  630.0   643.0  608.0

[5586 rows x 6 columns]
```