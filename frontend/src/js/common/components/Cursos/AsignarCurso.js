import React from 'react';
import { Field, reduxForm } from "redux-form";
import { SelectField } from '../Utils/renderField/renderField';


const ExCursos = [
    { label: "Matematicas", value: "matematicas" },
    { label: "Ciencias", value: "ciencias" },
    { label: "Idiomas", value: "idiomas" },
];

const ExStudents = [
    { label: "Primary", value: "Primary" },
    { label: "Secondary", value: "Secondary" },
];


const Asignar = (props) => {
    const { handleSubmitAsignar } = props;
    return (
        <form name="asignaForm" className="form-validate mb-lg" onSubmit={handleSubmitAsignar}>
            <div>
                <div className="mb-3 col-12">
                    <strong className="text-muted d-block mb-2">Asignar</strong>
                    <div className="row">
                        <div className="col-12 mb-2">
                            <label htmlFor="select_curso">Selecciona curso</label>
                            <Field
                                name="select_curso"
                                options={ExCursos}
                                component={SelectField}
                            />
                        </div>
                        <div className="col-12 mb-2">
                            <label htmlFor="select_estudiante">Selecciona estudiante</label>
                            <Field
                                name="select_estudiante"
                                options={ExStudents}
                                component={SelectField}
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
    form: 'asignaForm',
})(Asignar);
