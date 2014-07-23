puts 'GDB Remote protocol parser'

content = File.read("example.file")
packets = content.split('$')
puts 'Packets count: %d' % packets.length