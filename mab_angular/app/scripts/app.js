'use strict';

/**
 * @ngdoc overview
 * @name mab
 * @description
 * # mab
 *
 * Main module of the application.
 */
angular
  .module('mab', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
  ])
  .config(function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
      })
      .when('/users', {
        templateUrl: 'views/users.html',
        controller: 'UsersController'
      })
      .when('/_header', {
        templateUrl: 'views/header.html'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
