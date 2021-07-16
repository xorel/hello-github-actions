#!/usr/bin/ruby
#
def set_output(name, content)
    # escape content
    esc = content.gsub("%", '%25')
    esc.gsub!("\n", '%A0')
    esc.gsub!("\r", '%D0')

    puts "::set-output name=#{name}::\"#{esc}\""
end

puts "AAA"
puts "BBB"


set_output("test1", "abc")
set_output("test2", "aaa\nbbb")
set_output("test3", "aaa\nbbb\nccc")

