project(
  'sdnotify-wrapper-py',
  version: run_command('./get_version', check: true).stdout().strip()
)

meson.add_dist_script('./get_version', '--save')

py = import('python').find_installation()

py.install_sources('sdnotify_wrapper.py')
