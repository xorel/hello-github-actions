#!/usr/bin/ruby

require "faraday"
require "json"


RSpec.describe 'One-hosted test' do

    it 'response on http 1' do
        resp = Faraday.get('http://demo.opennebula.com/')
        expect(resp.status).to eq 200
    end

    it 'response on http 1' do
        resp = Faraday.get('http://demo.opennebula.com/')
        expect(resp.status).to eq 200
    end
end


