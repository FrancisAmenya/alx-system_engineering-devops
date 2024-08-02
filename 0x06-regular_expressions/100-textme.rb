#!/usr/bin/env ruby
# Match Sender, Reciever and flags from 
# Message logs

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(',')
