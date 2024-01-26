Bliss Writer
============

The `blisswriter` project provides NeXus-compliant HDF5 file writing based on
data published by `blissdata`. It can be used in three ways

* writer service for a single `bliss` session as a *process*
  * command line interface: `NexusSessionWriter`
  * consumer of Redis data published by `blissdata`
* writer service for a single `bliss` session as a *Tango device*
  * command line interface: `NexusWriterService`
  * consumer of Redis data published by `blissdata`
* writer python API
  * python API: `from blisswriter.writer.main import ScanWriterWithState`
  * same API used by the writer services

`blisswriter` is developed and maintained by the [Software group](https://www.esrf.fr/Instrumentation/software)
of the [European Synchrotron](https://www.esrf.fr/).
