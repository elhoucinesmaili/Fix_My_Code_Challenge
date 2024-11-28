###
#  Sort integer arguments (ascending) 
###

result = []

ARGV.each do |arg|
  # Skip if not an integer
  next unless arg.match?(/^-?\d+$/)

  # Convert to integer and insert into the result array
  result.push(arg.to_i)
end

# Sort the array
result.sort!

# Output the sorted result
puts result
