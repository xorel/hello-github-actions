#!/usr/bin/ruby

require "faraday"
require "json"

resp =  Faraday.get('http://demo.opennebula.com/')
pp resp.status
