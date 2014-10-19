'use strict';

(function() {
  angular.module('mab')
    .controller('BetSubjectList', ['bets', BetSubjectList]);

  function BetSubjectList(bets) {
    var vm = this;
    vm.list = bets.BetSubject.query();
  }

})();
