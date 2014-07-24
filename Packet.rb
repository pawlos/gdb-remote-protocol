class Packet
    def initialize(content)
        @content = content
    end

    def print
        puts @content
    end

    def is_valid
        sum = 0
        hash = @content.index('#')
        string_array = @content.split()
        string_array[0, hash].each do |e| 
            sum += e.ord
        end
        return sum == @content[hash+1, 2].hex
    end
end