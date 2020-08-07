import React from 'react';
import { Field, reduxForm } from 'redux-form';
import { renderField } from "Utils/renderField/renderField";


const CrearCurso = (props) => {
    const { crearCurso } = props;
    return (
        <form
            name="cursoForm"
            className="form-validate mb-lg"
            onSubmit={crearCurso}
        >
            <div className="row">
                <div className="col-lg-12">
                    <h4>Escribe el nombre del curso</h4>
                    <div className="row">
                        <div className="col-lg-12">
                            <label htmlFor=""> Titulo </label>
                            <Field
                                name="titulo"
                                label="Titulo"
                                component={renderField}
                                type="text"
                                className="form-control"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className="row mb-5 mt-4">
                <div className="col-lg-12 d-flex justify-content-end">
                    <button
                        type="submit"
                        className="btn btn-primary"
                    >
                                    ENVIAR
                    </button>
                </div>
            </div>
        </form>
    );
};

export default reduxForm({
    form: 'cursoForm',
})(CrearCurso);
