(function() {
  angular.module('mab')
    .controller('SignUpCtrl', ['$location', 'users', SignUpCtrl]);

  function SignUpCtrl($location, users) {
    var vm = this;
    vm.signup = signup;
    vm.user = {};

    function signup() {
      if (vm.user.password === vm.user.password2) {
        users.signup(vm.user.email, vm.user.password).then(success, error);
      } else {
        /*jshint camelcase: false*/
        vm.errors = {non_field_errors: 'passwords are not equal'};
      }

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
