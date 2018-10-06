#!/bin/bash

base_dir=$(pwd)
api_dir=$base_dir/api/
ui_dir=$base_dir/ui/
api_main_file=main.py

function run_api()
{
  cd ${api_dir}
  FLASK_APP=${api_main_file} flask run
}

function run_ui()
{
  cd ${ui_dir}
  ng serve
}

case "$1" in
  api)
    run_api
    ;;
  ui)
    run_ui
    ;;
  *)
    echo Improper Command
    ;;
esac
