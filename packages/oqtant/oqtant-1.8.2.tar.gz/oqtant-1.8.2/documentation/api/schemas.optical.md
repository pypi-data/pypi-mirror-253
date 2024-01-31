<!-- markdownlint-disable -->

<a href="../../oqtant/schemas/optical.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `schemas.optical`






---

<a href="../../oqtant/schemas/optical.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Snapshot`
A class that represents a painted optical landscape/potential at a single point in (manipulation stage) time 


---

#### <kbd>property</kbd> interpolation_kind





---

#### <kbd>property</kbd> model_computed_fields

Get the computed fields of this model instance. 



**Returns:**
  A dictionary of computed field names and their corresponding `ComputedFieldInfo` objects. 

---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="../../oqtant/schemas/optical.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_input`

```python
from_input(landscape: 'Landscape') → Snapshot
```

Method to create a Snapshot object from an existing jobs input 



**Args:**
 
 - <b>`landscape`</b> (bert_schemas.job.Landscape):  The input values 



**Returns:**
 
 - <b>`Snapshot`</b>:  A new Snapshot object created using the input data 

---

<a href="../../oqtant/schemas/optical.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ideal_potential`

```python
get_ideal_potential(
    time=0.0,
    positions: 'list' = array([-60., -59., -58., -57., -56., -55., -54., -53., -52., -51., -50.,
       -49., -48., -47., -46., -45., -44., -43., -42., -41., -40., -39.,
       -38., -37., -36., -35., -34., -33., -32., -31., -30., -29., -28.,
       -27., -26., -25., -24., -23., -22., -21., -20., -19., -18., -17.,
       -16., -15., -14., -13., -12., -11., -10.,  -9.,  -8.,  -7.,  -6.,
        -5.,  -4.,  -3.,  -2.,  -1.,   0.,   1.,   2.,   3.,   4.,   5.,
         6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.,
        17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.,  25.,  26.,  27.,
        28.,  29.,  30.,  31.,  32.,  33.,  34.,  35.,  36.,  37.,  38.,
        39.,  40.,  41.,  42.,  43.,  44.,  45.,  46.,  47.,  48.,  49.,
        50.,  51.,  52.,  53.,  54.,  55.,  56.,  57.,  58.,  59.,  60.])
) → list[float]
```

Method to get the ideal potential energy at the specified positions 



**Args:**
 
 - <b>`positions`</b> (list, optional):  List of positions in microns 



**Returns:**
 
 - <b>`list[float]`</b>:  Potential energies, in kHz, at the specified positions 

---

<a href="../../oqtant/schemas/optical.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_potential`

```python
get_potential(positions: 'list[float]') → list[float]
```

Method to calculate the optical potential associated with a Landscape object, taking into account the actual implementation of the Oqtant projection system, at the given time 



**Args:**
 
 - <b>`positions`</b> (list[float]):  Positions, in microns, where the potential should be evaluated 



**Returns:**
 
 - <b>`list[float]`</b>:  Potential energies, in kHz, at the specified positions 

---

<a href="../../oqtant/schemas/optical.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `new`

```python
new(
    time: 'float' = 0,
    positions: 'list' = [-10, 10],
    potentials: 'list' = [0, 0],
    interpolation: 'InterpolationType' = 'LINEAR'
) → Snapshot
```

Method to create a new Snapshot object 



**Args:**
 
 - <b>`time`</b> (float, optional):  Time associated with the snapshot 
 - <b>`positions`</b> (list, optional):  Position list for the snapshot 
 - <b>`potentials`</b> (list, optional):  Potential energies corresponding to the list of positions 
 - <b>`interpolation`</b> (bert_schemas.job.InterpolationType, optional):  How to connect the object's  (positions, potentials) data in space. 



**Returns:**
 
 - <b>`Snapshot`</b>:  a new Snapshot object 

---

<a href="../../oqtant/schemas/optical.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_potential`

```python
show_potential(
    xlimits: 'list[float]' = [-61.0, 61],
    ylimits: 'list[float]' = [-1.0, 101],
    include_ideal: 'bool' = False
) → None
```

Method to plot the potential energy as a function of position for a Landscape object at the given times 



**Args:**
 
 - <b>`xlimits`</b> (list[float], optional):  Plot limits for x axis 
 - <b>`ylimits`</b> (list[float], optional):  Plot limits for y axis 
 - <b>`include_ideal`</b> (bool, optional):  Flag for including target potential in plot 


---

<a href="../../oqtant/schemas/optical.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Landscape`
Class that represents a dynamic painted-potential optical landscape constructed from individual (instantaneous time) Snapshots 


---

#### <kbd>property</kbd> interpolation_kind





---

#### <kbd>property</kbd> model_computed_fields

Get the computed fields of this model instance. 



**Returns:**
  A dictionary of computed field names and their corresponding `ComputedFieldInfo` objects. 

---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 

---

#### <kbd>property</kbd> snapshots

Property to get a list of Snapshot objects associated to a Landscape object 



**Returns:**
 
 - <b>`list[Snapshot]`</b>:  List of Snapshot objects 



---

<a href="../../oqtant/schemas/optical.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_input`

```python
from_input(landscape: 'OpticalLandscape') → Landscape
```

Method to create a Landscape object from an existing jobs input 



**Args:**
 
 - <b>`landscape`</b> (job_schema.OpticalLandscape):  The input values 



**Returns:**
 
 - <b>`Landscape`</b>:  A new Landscape object 

---

<a href="../../oqtant/schemas/optical.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ideal_potential`

```python
get_ideal_potential(
    time: 'float',
    positions: 'list[float]' = array([-60., -59., -58., -57., -56., -55., -54., -53., -52., -51., -50.,
       -49., -48., -47., -46., -45., -44., -43., -42., -41., -40., -39.,
       -38., -37., -36., -35., -34., -33., -32., -31., -30., -29., -28.,
       -27., -26., -25., -24., -23., -22., -21., -20., -19., -18., -17.,
       -16., -15., -14., -13., -12., -11., -10.,  -9.,  -8.,  -7.,  -6.,
        -5.,  -4.,  -3.,  -2.,  -1.,   0.,   1.,   2.,   3.,   4.,   5.,
         6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.,
        17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.,  25.,  26.,  27.,
        28.,  29.,  30.,  31.,  32.,  33.,  34.,  35.,  36.,  37.,  38.,
        39.,  40.,  41.,  42.,  43.,  44.,  45.,  46.,  47.,  48.,  49.,
        50.,  51.,  52.,  53.,  54.,  55.,  56.,  57.,  58.,  59.,  60.])
) → list[float]
```

Method to calculate ideal object potential energy at the specified time and positions 



**Args:**
 
 - <b>`time`</b> (float):  Time, in ms, at which the potential energy is calculated 
 - <b>`positions`</b> (list[float], optional):  Positions at which the potential energy is calculated 



**Returns:**
 
 - <b>`list[float]`</b>:  Potential energies, in kHz, at specified time and positions 

---

<a href="../../oqtant/schemas/optical.py#L240"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_potential`

```python
get_potential(
    time: 'float',
    positions: 'list' = array([-60., -59., -58., -57., -56., -55., -54., -53., -52., -51., -50.,
       -49., -48., -47., -46., -45., -44., -43., -42., -41., -40., -39.,
       -38., -37., -36., -35., -34., -33., -32., -31., -30., -29., -28.,
       -27., -26., -25., -24., -23., -22., -21., -20., -19., -18., -17.,
       -16., -15., -14., -13., -12., -11., -10.,  -9.,  -8.,  -7.,  -6.,
        -5.,  -4.,  -3.,  -2.,  -1.,   0.,   1.,   2.,   3.,   4.,   5.,
         6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.,
        17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.,  25.,  26.,  27.,
        28.,  29.,  30.,  31.,  32.,  33.,  34.,  35.,  36.,  37.,  38.,
        39.,  40.,  41.,  42.,  43.,  44.,  45.,  46.,  47.,  48.,  49.,
        50.,  51.,  52.,  53.,  54.,  55.,  56.,  57.,  58.,  59.,  60.])
) → list[float]
```

Method to calculate the optical potential associated with a Landscape object, taking into account the actual implementation of the Oqtant projection system, at the given time 



**Args:**
 
 - <b>`time`</b> (float):  Time, in ms, at which to sample the potential energy 
 - <b>`positions`</b> (list[float], optional):  Positions, in microns, where the potential should be evaluated 



**Returns:**
 
 - <b>`list[float]`</b>:  Potential energies, in kHz, at the requested positions and time 

---

<a href="../../oqtant/schemas/optical.py#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `new`

```python
new(
    snapshots: 'list[Snapshot]' = [Snapshot(time_ms=0.0, potentials_khz=[0.0, 0.0], positions_um=[-10.0, 10.0], spatial_interpolation=<InterpolationType.LINEAR: 'LINEAR'>, interpolation_kind='linear'), Snapshot(time_ms=2.0, potentials_khz=[0.0, 0.0], positions_um=[-10.0, 10.0], spatial_interpolation=<InterpolationType.LINEAR: 'LINEAR'>, interpolation_kind='linear')]
) → Landscape
```

Method to create a new Landscape object 



**Args:**
 
 - <b>`snapshots`</b> (list[Snapshot], optional):  A list of Snapshot objects 



**Returns:**
 
 - <b>`Landscape`</b>:  A new Landscape object 

---

<a href="../../oqtant/schemas/optical.py#L258"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_potential`

```python
show_potential(
    times: 'list' = [0.0],
    xlimits: 'list' = [-61.0, 61],
    ylimits: 'list' = [-1.0, 101],
    include_ideal: 'bool' = False
)
```

Method to plot the potential energy as a function of position for a Landscape object at the given times 



**Args:**
 
 - <b>`times`</b> (list[float], optional):  Times, in ms, at which to evaluate and plot the potential 
 - <b>`xlimits`</b> (list[float], optional):  Plot limits for x axis 
 - <b>`ylimits`</b> (list[float], optional):  Plot limits for y axis 
 - <b>`include_ideal`</b> (bool, optional):  Flag for including target potential in plot 


---

<a href="../../oqtant/schemas/optical.py#L303"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Barrier`
Class that represents a painted optical barrier. 


---

#### <kbd>property</kbd> birth

Property to get the (manipulation stage) time that the Barrier object will be created 



**Returns:**
 
 - <b>`float`</b>:  The time, in ms, at which the barrier will start being projected 

---

#### <kbd>property</kbd> death

Property to get the (manipulation stage) time that the Barrier object will cease to exist 



**Returns:**
 
 - <b>`float`</b>:  The time, in ms, at which the barrier will stop being projected 

---

#### <kbd>property</kbd> interpolation_kind





---

#### <kbd>property</kbd> lifetime

Property to get the lifetime value of a Barrier object 



**Returns:**
 
 - <b>`float`</b>:  The amount of time, in ms, that the barrier will exist 

---

#### <kbd>property</kbd> model_computed_fields

Get the computed fields of this model instance. 



**Returns:**
  A dictionary of computed field names and their corresponding `ComputedFieldInfo` objects. 

---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="../../oqtant/schemas/optical.py#L348"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_input`

```python
from_input(barrier: 'Barrier') → Barrier
```

Method to create a Barrier object using the input values of a job 



**Args:**
 
 - <b>`barrier`</b> (job_schema.Barrier):  The input values 



**Returns:**
 
 - <b>`Barrier`</b>:  A new Barrier object created using the input data 

---

<a href="../../oqtant/schemas/optical.py#L306"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `new`

```python
new(
    positions: 'list[float]' = [0.0, 0.0],
    heights: 'list[float]' = [0.0, 0.0],
    widths: 'list[float]' = [1.0, 1.0],
    times: 'list[float]' = [0.0, 10.0],
    shape: 'ShapeType' = <ShapeType.GAUSSIAN: 'GAUSSIAN'>,
    interpolation: 'InterpolationType' = <InterpolationType.LINEAR: 'LINEAR'>
) → Barrier
```

Method to create a new Barrier object 



**Args:**
 
 - <b>`positions`</b> (list[float], optional):  Positions for the barrier 
 - <b>`heights`</b> (list[float], optional):  Heights for the barrier 
 - <b>`widths`</b> (list[float], optional):  Widths for the barrier 
 - <b>`times`</b> (list[float], optional):  Times for the barrier 
 - <b>`shape`</b> (bert_schemas.job.ShapeType, optional):  Shape of the barrier 
 - <b>`interpolation`</b> (bert_schemas.job.InterpolationType, optional):  Interpolation type of the barrier 



**Returns:**
 
 - <b>`Barrier`</b>:  A new Barrier object 



**Raises:**
 
 - <b>`ValueError`</b>:  if data lists are not of equal length 

---

<a href="../../oqtant/schemas/optical.py#L360"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_dynamics`

```python
show_dynamics() → None
```

Method to plot the position, width and height of a Barrier object over time 

---

<a href="../../oqtant/schemas/optical.py#L407"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_potential`

```python
show_potential(
    times: 'list[float]' = [0.0],
    xlimits: 'list[float]' = [-61.0, 61],
    ylimits: 'list[float]' = [-1.0, 101],
    include_ideal: 'bool' = False
) → None
```

Method to plot the potential energy as a function of position for a Barrier object 



**Args:**
 
 - <b>`times`</b> (list[float], optional):  The times, in ms, at which the potential is evaluated 
 - <b>`xlimits`</b> (list[float], optional):  Plot limits for x axis 
 - <b>`ylimits`</b> (list[float], optional):  Plot limits for y axis 
 - <b>`include_ideal`</b> (bool, optional):  Flag for including target potential in plot 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
