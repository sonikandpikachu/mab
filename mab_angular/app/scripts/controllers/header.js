'use strict';

/**
 * @ngdoc function
 * @name mab.controller:HeaderController
 * @description
 * # HeaderController
 * Controller of the mab
 */
angular.module('mab')

.controller('HeaderController', ['$scope', '$location', function($scope, $location) {
  $scope.hrefs = [
    {href: '#/about', name: 'About', active: ''},
    {href: '#/signup', name: 'Registration', active: ''},
    {href: '#/', name: 'Home', active: 'active'},
  ];

  $scope.loc = $location.path();

  $scope.$on('$locationChangeSuccess', function() {
    angular.forEach($scope.hrefs, function(value) {
      var path = $location.path();
      if (value.href.indexOf(path, value.href.length - path.length) !== -1) {
        value.active = 'active';
        console.log(value.href + ' ' + value.active);
      } else {
        value.active = '';
      }
    });
  });

}]);
