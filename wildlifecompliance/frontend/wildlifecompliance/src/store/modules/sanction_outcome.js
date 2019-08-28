import Vue from 'vue';
import {
    api_endpoints,
    helpers
}
from '@/utils/hooks';

export const sanctionOutcomeStore = {
    namespaced: true,
    state: {
        sanction_outcome: {
            
        },
    },
    getters: {
        sanction_outcome: state => state.sanction_outcome,
    },
    mutations: {
        updateSanctionOutcome(state, sanction_outcome) {
            console.log('updateSanctionOutcome');
            console.log(sanction_outcome);
            Vue.set(state, 'sanction_outcome', {
                ...sanction_outcome
            });
            if (state.sanction_outcome.date_of_issue) {
                state.sanction_outcome.date_of_issue = moment(state.sanction_outcome.date_of_issue, 'YYYY-MM-DD').format('DD/MM/YYYY');
            }
        },
    },
    actions: {
        async loadSanctionOutcome({ dispatch, }, { sanction_outcome_id }) {
            console.log("loadSanctionOutcome");
            try {
                const returnedSanctionOutcome = await Vue.http.get(
                    helpers.add_endpoint_json(
                        api_endpoints.sanction_outcome, 
                        sanction_outcome_id)
                    );
                await dispatch("setSanctionOutcome", returnedSanctionOutcome.body);
            } catch (err) {
                console.log(err);
            }
        },
        async saveSanctionOutcome({ dispatch, state }, { route, crud, internal }) {
            console.log(crud)
            let sanctionOutcomeId = null;
            let savedSanctionOutcome = null;
            try {
                let fetchUrl = null;
                if (crud === 'create' || crud === 'duplicate') {
                    fetchUrl = api_endpoints.sanction_outcome;
                } else {
                    fetchUrl = helpers.add_endpoint_join(
                        api_endpoints.sanction_outcome, 
                        state.sanction_outcome.id + "/sanction_outcome_save/"
                        )
                }

                let payload = {};
                Object.assign(payload, state.sanction_outcome);
                if (crud == 'duplicate') {
                    payload.id = null;
                    payload.location_id = null;
                    if (payload.location) {
                        payload.location.id = null;
                    }
                }

                savedSanctionOutcome = await Vue.http.post(fetchUrl, payload);
                await dispatch("setSanctionOutcome", savedSanctionOutcome.body);
                sanctionOutcomeId = savedSanctionOutcome.body.id;

            } catch (err) {
                console.log(err);
                if (internal) {
                    // return "There was an error saving the record";
                    return err;
                } else {
                    await swal("Error", "There was an error saving the record", "error");
                }
                return window.location.href = "/internal/sanction_outcome/";
            }
            if (crud === 'duplicate') {
                return window.location.href = "/internal/sanction_outcome/" + sanctionOutcomeId;
            }
            else if (crud !== 'create') {
                if (!internal) {
                    await swal("Saved", "The record has been saved", "success");
                } else {
                    return savedSanctionOutcome;
                }
            }
            if (route) {
                return window.location.href = "/internal/sanction_outcome/";
            } else {
                return sanctionOutcomeId;
            }
        },
        setSanctionOutcome({ commit, }, sanction_outcome) {
            commit("updateSanctionOutcome", sanction_outcome);
        },
    },
}