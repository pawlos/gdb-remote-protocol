import sys

readingMem = False
addr = 0x0
#pr = lambda x: print x
def decode(m):
  #print 'Enter: ',m
  result = ""
  index = 0
  while '*' in m:
    n_index = m.index('*')
    result += m[0:n_index]
    #print 'C: ',result
    what = m[n_index-1]
    how_many = ord(m[n_index+1]) - 29
    result += what * how_many
    m = m[n_index+2:]
    #print 'm: ',m
    index = n_index+1
    #print 'Current result is: ',result
  return result+m[0:]

def readMem(m):
   global readingMem
   global addr
   checksum = m[1:].index('#')
   split = m[1:1+checksum].split(',')
   print 'Reading memory at: 0x'+split[0]+' of 0x'+split[1]+' bytes'
   readingMem = True #if '55555555' in split[0] else False
   addr = int(split[0],16)
   #print 'Addr: ',addr

def readRegs(x):
   print 'Reading registers', x

def qSymbol(x):
  checksum = x.index('#')
  x = x[0:checksum]
  x = x.replace('qSymbol','')
  x = x.replace(':','')
  #print 'q: ',decode(x)
  return decode(x).decode('hex')

def vFile(x):
  option = x[6:x.index(':',6)]
  if option == 'open':
    #print 'vfile:',x[11:x.index(',')]
    return 'open: '+x[11:x.index(',')].decode('hex')+" "+x[x.index(','):]
  return x

with open('data.file') as f, open('a.out','wb') as g:

  data = f.read()

  packets = data.split('$')
  mappings = {
   '!': lambda x: sys.stdout.write('Extended mode, '+x+'\n'),
   '+': lambda x: sys.stdout.write(''),
   'm': lambda x: readMem(x),
   'g': lambda x: readRegs(x),
   'qSymbol': lambda x: sys.stdout.write('qSymbol: '+qSymbol(x)+'\n'),#[8:].decode('hex'),
   'qSupported': lambda x: sys.stdout.write(x),
   'PacketSize': lambda x: sys.stdout.write(x),
   'vFile': lambda x: sys.stdout.write('File: '+vFile(x)+'\n')
}

  for p in packets:
    packet_type = p[0]
    if packet_type in mappings:
      mappings[packet_type](p)
      continue
    else:
      if ':' in p:
        packet_type = p[0:p.index(':')]
        if packet_type in mappings:
         mappings[packet_type](p)
         continue

    data = decode(p[:p.index('#')])
    sys.stdout.write('Unk: '+data+'\n')
    base = 0x555555554000
    if readingMem:
     readingMem = False
     if '55555555' in hex(addr):
      sys.stdout.write('Saving @: '+str(addr-base)+'\n')
      g.seek(addr-base) 
      g.write(data.decode('hex'))
    try:
      sys.stdout.write(data.decode('hex')+'\n')  
    except:
      pass
  sys.stdout.flush() 
