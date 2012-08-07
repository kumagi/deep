name='deep'
def options(opt):
  opt.load('compiler_cxx')

def configure(conf):
  conf.env.CXXFLAGS += ['-O2', '-Wall', '-g', '-pipe']
  conf.load('compiler_cxx')

  conf.check_cxx(lib = 'msgpack', mandatory = True)
  conf.check_cxx(lib = 'glog', mandatory = True)

  conf.check_cxx(lib = 'pficommon', mandatory = True)
  conf.check_cxx(lib = 'pficommon_system', mandatory = True)
  conf.check_cxx(lib = 'pficommon_concurrent', mandatory = True)
  conf.check_cxx(lib = 'pficommon_network_mprpc', mandatory = True)
  conf.check_cxx(lib = 'pficommon_math', mandatory = True)

  conf.check_cxx(lib = 'jubatus_framework', mandatory = True)
  conf.check_cxx(lib = 'jubacommon', mandatory = True)
  conf.check_cxx(lib = 'jubacommon_mprpc', mandatory = True)

def build(bld):
  bld.program(
    source = name+'_serv.cpp '+ name +'_impl.cpp',
    target = name,
    use = ['JUBATUS_FRAMEWORK', 'JUBACOMMON', 'JUBACOMMON_MPRPC', 'PFICOMMON', 'PFICOMMON_CONCURRENT',
           'PFICOMMON_NETWORK_MPRPC', 'PFICOMMON_SYSTEM', 'MSGPACK',
           'GLOG']
    )

  bld.program(
    source = name+'_keeper.cpp',
    target = name+'_keeper',
    use = ['JUBATUS_FRAMEWORK', 'JUBACOMMON', 'JUBACOMMON_MPRPC', 'PFICOMMON', 'PFICOMMON_CONCURRENT',
           'PFICOMMON_NETWORK_MPRPC', 'PFICOMMON_SYSTEM', 'PFICOMMON_MATH', 'MSGPACK',
           'GLOG']
    )
