#ifndef DEEP_SERV_HPP_
#define DEEP_SERV_HPP_

#include <jubatus/framework.hpp>
#include <pficommon/data/unordered_map.h>
#include "deep_types.hpp"
#include <deque>
#include <vector>

using namespace jubatus::framework;
using namespace jubatus;

namespace jubatus { namespace server {

class deep_serv : public jubatus_serv {
public:
  deep_serv(const server_argv& a);
  virtual ~deep_serv();

  int query(const std::string&);
  
  void after_load();
private:
  size_t ema_short_length_;
  size_t ema_long_length_;
  typedef std::vector<int> window_t;
  typedef std::map<std::string, window_t> ema_table_t;
  ema_table_t ema_table_;
};


}} // namespace jubatus::server

#endif // DEEP_SERV_HPP_
