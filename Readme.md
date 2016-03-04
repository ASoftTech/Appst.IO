# Appst.IO

## Overvew

This is a series of Input / Output libraries that can be used under .Net.

  * There's code for a serial port that Reactive Extensions for streaming the data.
  * The serial port code also has support for IObservable for binding to controls
  * There's code for launching process's which wrappers the standard input and standard output using reactive extensions.

  * Appst.IO.Serial - serial port library
  * Appst.Reactive - base class's for reactive extensions
  * Appst.IO.Serial.Reactive - this includes observable class's for data binding and the use of reactive extensions for streaming data
  * Appst.Diagnostics.Process.Reactive - adds a layer on top of System.Diagnostics.Process for reactive process's
