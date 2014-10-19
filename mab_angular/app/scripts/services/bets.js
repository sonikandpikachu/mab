'use strict';

(function() {
  angular.module('mab')
    .service('bets', ['API', '$resource', '$http', bets]);

  function bets(API, $resource, $http) {
    /*jshint validthis: true */
    var vm = this;

    vm.BetSubject = $resource(API + 'bet-subjects/');
    vm.makeBet = makeBet;

    function makeBet(description, betSubjectPk) {
      return $http.post(API + 'bet-subjects/' + betSubjectPk, {description: description});
    }

  }

})();
