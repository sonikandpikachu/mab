'use strict';

/**
 * @ngdoc function
 * @name mab.controller:usersController
 * @description
 * # usersController
 * Controller of the mab
 */
angular.module('mab')

.controller('UsersController', ['$scope', 'Users', function($scope, Users) {
  $scope.user = Users.get({id: 4});
}]);
