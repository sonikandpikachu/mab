'use strict';

(function() {
  angular.module('mab')
    .controller('HeaderCtrl', ['$scope', '$location', 'users', HeaderCtrl]);

  function HeaderCtrl($scope, $location, users) {
    var vm = this;
    vm.loc = $location.path();
    vm.user = users.user;
    vm.hrefs = hrefs();
    vm.signout = signout;

    $scope.$on('$locationChangeSuccess', chooseActiveHref);
    $scope.$watch(function() { return users.user; }, initHrefs);

    function initHrefs(user) {
      vm.user = user;
      vm.hrefs = hrefs();
    }

    function hrefs() {
      var _hrefs = null;
      if (users.user.isAuthenticated) {
        _hrefs = [
          {href: '#/about', name: 'About', active: ''},
          {href: '#/bet-subjects', name: 'Bets', active: ''},
          {href: '#/', name: 'Home', active: 'active'},
        ];
      } else {
        _hrefs = [
          {href: '#/', name: 'Home', active: 'active'},
        ];
      }
      return _hrefs;
    }

    function chooseActiveHref() {
      angular.forEach(vm.hrefs, chooseActive);
    }

    function chooseActive(value) {
      var path = $location.path();
      if (value.href.indexOf(path, value.href.length - path.length) !== -1) {
        value.active = 'active';
      } else {
        value.active = '';
      }
    }

    function signout() {
      users.signout();
      $location.path('/');
    }

  }

})();
