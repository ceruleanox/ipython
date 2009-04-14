"""Simple script to show reference holding behavior.

This is used by a companion test case.
"""

import gc

class C(object):
   def __del__(self):
      pass
      #print 'deleting object...'  # dbg

c = C()

c_refs = gc.get_referrers(c)
ref_ids = map(id,c_refs)

print 'c referrers:',map(type,c_refs)
