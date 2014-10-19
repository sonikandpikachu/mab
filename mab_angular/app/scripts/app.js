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

      .when('/_header', {
        templateUrl: 'views/header.html'
      })

      // users
      .when('/signin', {
        templateUrl: 'views/signin.html',
      })

      .when('/signup', {
        templateUrl: 'views/signup.html',
      })

      // bets
      .when('/bet-subjects', {
        templateUrl: 'views/bet-subjects.html',
        controller: 'BetSubjectList',
        controllerAs: 'betSubjectList'
      })

      .otherwise({
        redirectTo: '/'
      });
  });
