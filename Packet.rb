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
        string_array = @content.split(//)[0, hash]
        string_array.each do |e| 
            sum += e.ord
        end

        return (sum % 256) == @content[hash+1, 2].hex
    end
end