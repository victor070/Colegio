import { handleActions } from 'redux-actions';
import { api } from "api";
import { NotificationManager } from "react-notifications";
import { push } from "react-router-redux";

const SUBMIT = 'LOGIN_SUBMIT';
const CURSOS_LOADER = 'CURSOS_LOADER';
const CURSO = 'LOGIN_CURSO';

export const constants = {
    SUBMIT,
};

// ------------------------------------
// Pure Actions
// ------------------------------------

export const setLoader = loader => ({
    type: CURSOS_LOADER,
    loader,
});

export const setMe = me => ({
    type: CURSO,
    me,
});
// ------------------------------------
// Actions
// ------------------------------------

export const listar = (page = 1) => (dispatch) => {
    console.log("estoy aqui");
    const params = { page };
    dispatch(setLoader(true));
    api.get('/curso', params).then((data) => {
        if (data) {
            console.log("estos son los cursos: ", data);
        }
    }).catch(() => {
    }).finally(() => {
        dispatch(setLoader(false));
    });
};

export const crearCurso = (data = {}) => (dispatch) => {
    console.log('estoy aqui');
    dispatch(setLoader(true));
    api.post('curso', data).then(() => {
        NotificationManager.success('Registro creado', 'Éxito', 3000);
    }).catch(() => {
        NotificationManager.error('Error en la creación', 'ERROR');
    }).finally(() => {
        dispatch(setLoader(false));
    });
};

export const getMe = () => (dispatch) => {
    api.get('curso').then((me) => {
        dispatch(setMe(me));
    })
        .catch(() => {
        }).finally(() => {});
};

export const crearNota = (data = {}) => (dispatch) => {
    console.log('estoy aqui');
    dispatch(setLoader(true));
    api.post('nota', data).then(() => {
        dispatch(push("/nota"));
        NotificationManager.success('Nota creada con éxito', 'Éxito', 3000);
    }).catch(() => {
        NotificationManager.error('Datos incorrectos, vuelva a intentar', 'ERROR', 0);
    }).finally(() => {
        dispatch(setLoader(false));
    });
};

export const actions = {
    listar,
    crearCurso,
    crearNota,
};

export const reducers = {
    [CURSOS_LOADER]: (state, { loader }) => {
        return {
            ...state,
            loader,
        };
    },
    [CURSO]: (state, { me }) => {
        return {
            ...state,
            me,
        };
    },
};

export const initialState = {
    loader: false,
    me: {},
};

export default handleActions(reducers, initialState);
