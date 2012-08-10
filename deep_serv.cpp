#include "deep_serv.hpp"
namespace jubatus { namespace server { // do not change

using namespace jubatus::framework;

deep_serv::deep_serv(const server_argv& a)
  :jubatus_serv(a){}

deep_serv::~deep_serv(){}

/*
std::vector<int> deep_serv::query(const std::string&){
	std::vector<int> test;
	test.push_back(54);
	return test;
}
//*/
int deep_serv::query(const std::string&){	return 42;}

void deep_serv::after_load(){}

}} // namespace jubatus::server
