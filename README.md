An example implementation of sync serial block
====

This uses threading module of python to synchronize 
data flow between serial block and input block using pipes

The usual place to use this is
| Fast Source | --> | Buffer Block | --> | Slow sink |
