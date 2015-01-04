require 'rubygems'
require 'sinatra'
require 'app'
get('/') { open('public/index.html').read }
run Sinatra::Application
