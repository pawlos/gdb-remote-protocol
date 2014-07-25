require_relative "Packet"
require "test/unit"

class TestPacket < Test::Unit::TestCase

	def test_when_provided_correct_input_is_valid_returns_true
		packet = Packet.new('qfThreadInfo#bb')
		assert_equal(true, packet.is_valid)
	end

	def test_when_provided_incorrect_input_is_valid_returns_false
		packet = Packet.new('E00#a6')
		assert_equal(false, packet.is_valid)
	end
end