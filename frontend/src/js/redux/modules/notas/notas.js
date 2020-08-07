import { handleActions } from 'redux-actions';
import { api } from "api";

const SUBMIT = 'REGISTER_SUBMIT';
const LOADER = 'REGISTER_LOADER';

export const constants = {
    SUBMIT,
};

// ------------------------------------
// Pure Actions
// ------------------------------------

export const setLoader = loader => ({
    type: LOADER,
    loader,
});

// ------------------------------------
// Actions
// ------------------------------------

export const listarNotas = (page = 1) => (dispatch) => {
    console.log("estoy aqui");
    const params = { page };
    dispatch(setLoader(true));
    api.get('/nota', params).then((data) => {
        if (data) {
            console.log("estos son las notas: ", data);
        }
    }).catch(() => {
    }).finally(() => {
        dispatch(setLoader(false));
    });
};


export const actions = {
    listarNotas,
};

export const reducers = {
    [LOADER]: (state, { loader }) => {
        return {
            ...state,
            loader,
        };
    },
};

export const initialState = {
    loader: false,
};

export default handleActions(reducers, initialState);
