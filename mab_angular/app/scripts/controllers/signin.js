'use strict';

(function() {
  angular.module('mab')
    .controller('SignInCtrl', ['$location', 'users', SignInCtrl]);

  function SignInCtrl($location, users) {
    var vm = this;
    vm.signin = signin;
    vm.user = {};

    function signin() {
      users.signin(vm.user.email, vm.user.password).then(success, error);

      function success() {
        $location.path('/');
      }

      function error(data) {
        var errors = {};
        for (var key in data.data) {
          if (data.data.hasOwnProperty(key)) {
            errors[key] = data.data[key][0];
          }
        }
        vm.errors = errors;
      }

    }
  }

})();
