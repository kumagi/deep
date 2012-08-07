#include "deep_serv.hpp"
namespace jubatus { namespace server { // do not change

using namespace jubatus::framework;

deep_serv::deep_serv(const server_argv& a)
  :jubatus_serv(a){}

deep_serv::~deep_serv(){}

int deep_serv::query(const std::string&){return 54;}

void deep_serv::after_load(){}

}} // namespace jubatus::server
