require './Packet'
require './BangPacket'

puts 'GDB Remote protocol parser'

content = File.read("example.file")
packets = content.split('$')
puts 'Packets count: %d' % packets.length
a = BangPacket.new('!#21+')
a.print
puts a.is_valid