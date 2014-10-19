'use strict';

(function() {
  angular.module('mab')
    .service('users', ['API', '$http', '$cookies', users]);

  function users(API, $http, $cookies) {
    /*jshint validthis: true */
    var vm = this;

    vm.signin = signin;
    vm.signup = signup;
    vm.signout = signout;
    vm.getCurrentUser = getCurrentUser;
    vm.getCurrentUserFromServer = getCurrentUserFromServer;
    vm.setAuthCookie = setAuthCookie;
    vm.getAuthCookie = getAuthCookie;
    vm.setAuthHeader = setAuthHeader;
    if (getAuthCookie() !== undefined){
      vm.user = {isAuthenticated: false};
    } else {
      vm.user = {isAuthenticated: true};
    }

    function signin(email, password) {
      var request = $http.post(API + 'signin/', {email: email, password: password})
        .then(success);

      function success(data) {
        vm.user = data.data;
        /*jshint camelcase: false*/
        setAuthCookie(vm.user.auth_token);
        vm.user.isAuthenticated = true;
      }

      return request;
    }

    function signup(email, password) {
      var request = $http.post(API + 'users/', {email: email, password: password})
        .then(success);

      function success(data) {
        vm.user = data;
        /*jshint camelcase: false*/
        setAuthCookie(vm.user.auth_token);
        vm.user.isAuthenticated = true;
      }

      return request;
    }

    function signout(){
      $cookies.token = undefined;
      delete $http.defaults.headers.common.Authorization;
      vm.user = {isAuthenticated: false};
    }

    function getCurrentUser() {
      if (vm.user.isAuthenticated) {
        return vm.user;
      } else {
        vm.user = getCurrentUserFromServer();
        return vm.user;
      }
    }

    function getCurrentUserFromServer() {
      var url = API + 'current-user/';
      $http.get(url).then(
        function(serverUser) {
          vm.user = serverUser;
          /*jshint camelcase: false*/
          setAuthCookie(vm.user.auth_token);
          vm.user.isAuthenticated = true;
        }
      );
    }

    function setAuthCookie(token) {
      $cookies.token = token;
      setAuthHeader(token);
    }

    function getAuthCookie() {
      return $cookies.token;
    }

    function setAuthHeader(token) {
      $http.defaults.headers.common.Authorization = 'Token ' + token;
      console.log('Token ' + token);
    }

  }

})();
