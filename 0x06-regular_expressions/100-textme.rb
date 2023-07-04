#!/usr/bin/env ruby
# returns SENDER,RECIEVER,FLAGS.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
