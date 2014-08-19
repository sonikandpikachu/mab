'use strict';

angular.module('mab')

.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }
])

.constant('API','http://127.0.0.1:8000/api/')

.factory('Users', ['$resource', 'API',
  function($resource, API) {
    return $resource(API + 'users/:id', {id: '@id'});
}]);
