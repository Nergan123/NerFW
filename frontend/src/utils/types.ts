export type LoginResponse = {
    token: string | null
    user: User | null
    message: string
    success: boolean
    statusCode: number
}

export type User = {
    id: number
    username: string
    role: string
}
