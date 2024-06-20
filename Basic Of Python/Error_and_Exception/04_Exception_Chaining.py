# Exception chaining is a technique of handling exceptions by re-throwing a caught exception after wrapping it inside a new exception.
try:
   open("nofile.txt")
except OSError as exc:
   raise RuntimeError from None