#!/bin/bash
echo "* \n* Running with 'minimal' config (excluding formats and tools sections) for faster updates...\n*"
export JEKYLL_CONFIG="_config.yml,_config-minimal.yml"

# Build for search:
#bundle exec jekyll 

#npx pagefind --site public --output-path static/pagefind

npx decap-server 2>/dev/null &
# Make sure this gets killed on exit:
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

bundle exec jekyll serve --watch --livereload --config $JEKYLL_CONFIG
