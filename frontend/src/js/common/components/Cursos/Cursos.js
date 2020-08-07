import React, { Component } from 'react';
import CrearCurso from './CrearCurso';
import AsignarCurso from './AsignarCurso';
import TablaCursos from './TablaCurso';


export default class Cursos extends Component {
    /* componentDidMount(props) {
        const { listar } = this.props;
        console.log(listar);
    } */

    componentWillMount() {
        console.log('props', this.props);
        console.log('curso');
    }

    crear = (values) => {
        console.log(values);
        console.log('props', this.props);
    }

    render() {
        const { crearCurso } = this.props;
        return (
            <div className="py-4">
                <h2>Cursos</h2>
                <div className="row">
                    <div className="mb-4 col-lg-12">
                        <div className="mb-4 card card-small">
                            <div className="border-bottom card-header d-flex justify-content-center">
                                <h3 className="m-0">Crear Curso</h3>
                            </div>
                            <div className="p-0 px-3 pt-3">
                                <CrearCurso onSubmit={crearCurso} />
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="mb-4 col-lg-12">
                        <div className="mb-4 card card-small">
                            <div className="border-bottom card-header d-flex justify-content-center">
                                <h3 className="m-0">Asignar Estudiantes</h3>
                            </div>
                            <div className="p-0 px-3 pt-3">
                                <AsignarCurso />
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="mb-4 col-lg-12">
                        <div className="mb-4 card card-small">
                            <div className="border-bottom card-header d-flex justify-content-center">
                                <h3 className="m-0">Tabla de curso y estudiantes</h3>
                            </div>
                            <div className="p-0 px-3 pt-3">
                                <TablaCursos />
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        );
    }
}
