#!/bin/bash
FIRST=0
SECOND=0
for i in $* ; do
  if [ $i -eq 3 ]; then FIRST=1 ; fi
  if [ $i -eq 6 ]; then SECOND=1 ; fi
done
if [ $FIRST -eq 1 ] ; then
  if [ $SECOND -eq 1 ] ; then
    exit 1 # interesting
  fi
fi
exit 0